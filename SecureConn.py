from paramiko import SSHClient, AutoAddPolicy

from getpass import getpass





class SecureConn:



    def __init__(self, user_name, ip_address, password) -> None:

        self._username = user_name

        self._ipaddress = ip_address

        self._password = password



    def read_parameters(self):

        self._username = input("Ingrese el nombre: ")

        self._ipaddress = input("Ingrese la direccion ip: ")

        self._password = getpass(prompt="Ingrese la contrasena: ")



    def conn_remote(self):

        self._client = SSHClient()

        self._client.set_missing_host_key_policy(AutoAddPolicy())

        self._client.load_system_host_keys()

        self._client.connect(

            hostname=self._ipaddress,

            username=self._username,

            password=self._password

        )



        print(f"Conexion exitosa con : {self._ipaddress}")



    def jobs_remote(self):

        self._client.invoke_shell()

        std_in, std_out, std_error = self._client.exec_command("pwd")

        print(f"{std_out.read}")

        self._client.exec_command("mkdir ~/Documentos/Prueba")

        self._client.exec_command("ls -l > ~/Documentos/Prueba/prueba.txt")

        std_in, std_out, std_error = self._client.exec_command(

            "ls -l ~Documentos/ | grep Prueba")

        print(f"{std_out.read()}")



    def close_conn(self):

        self._client.close





if __name__ == "__main__":

    secure_conn = SecureConn(

        user_name="",

        ip_address="",

        password=""

    )

    secure_conn.read_parameters()

    secure_conn.conn_remote()

    secure_conn.jobs_remote()

    secure_conn.close_conn()