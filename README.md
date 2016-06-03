# How To Configure the Oracle Connection Tester

## Create a configuration file

Copy `config.json.sample` to `config.json` and set the variables within:

`oracle_host` is the address of the Oracle host server.

`oracle_port` is the open port on the server, probably 1521.

`oracle_database` is the name of the database on the server.

`oracle_username` and `oracle_password` are the credentials we will use to authenticate with the database.

## Set up Oracle client and environment variables

If you don't already have an Oracle client installed on the machine:

- [download and install the Oracle Instant Client](http://www.oracle.com/technetwork/topics/winx64soft-089540.html). Get the **Instant Client Package - Basic Lite** and the **Instant Client Package - SDK** packages appropriate for your system and database version.
- Unzip the Instant Client into a directory, like `C:\Oracle\instantclient_11_1`
- Unzip the SDK and copy the `sdk` folder into that directory; so it will be at `C:\Oracle\instantclient_11_1\sdk`

Create an `ORACLE_HOME` environment variable that contains the Instant Client path:
1. `Control Panel` -> `System and Security` -> `System`
2. Click `Advanced System Settings` in the left panel
3. Click the `Environment Variables...` button
4. Click the `New...` button in either User or System variables.
5. Create a new variable named `ORACLE_HOME` and set its value to the client path, like `C:\Oracle\instantclient_11_1\`

And add that same path to the end of the `PATH` environment variable:
1. In the Environment Variables window (after steps 1-3 above), select the `Path` system variable in the bottom scroll window and click `Edit...`
2. To the end of `Variable` value, add the client path, like `;C:\Oracle\instantclient_11_1\`

If you already have an Oracle client installed on the machine, set `ORACLE_HOME` and append to `PATH` the appropriate path, like `C:\oracle\product\11.1.0\client_1\`
