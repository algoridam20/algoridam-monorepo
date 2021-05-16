# Basic shell commands

## Get os information

1. ### Get kernel info

    ```shell
    uname -a
    ```

2. ### Memory usage

    ```sell
    top
    ```

## Run processes

1. ### [Python script for ever](https://stackoverflow.com/questions/2975624/how-to-run-a-python-script-in-the-background-even-after-i-logout-ssh)

   ```shell
    nohup python bgservice.py &
    example$ nohup python3.7 -u notify-vaccine-availability.py > output.log &
   ```

   output in > nohup.output
2. ### Continuous tail
   
   ```shell
   tail -f filename
   ```

## ssh

1. set up ssh server [doc](https://dev.to/zduey/how-to-set-up-an-ssh-server-on-a-home-computer)
2. ip address in local network 
    ```shell
     arp -a
     ```
3. login with ssh 
    ```shell
    ssh username@ipaddress
    ```
4. file transfer
   ```shell
   scp source username@ipaddress:destination
   ```