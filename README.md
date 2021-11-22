# powerlogic-edge

Node JS application for SIMATIC WinCC Unified to read energy consumption from Schneider PowerLogic series over Modbus TCP/IP.

## Energy data

List of **PowerLogic** meter data:

| Measure                            | Units                 | Type          | 
| ---------------------------------- | --------------------- | ------------- | 
|  I1: phase 1 current               | A                     | Float32       | 
|  I2: phase 2 current               | A                     | Float32       |
|  I3: phase 3 current               | A                     | Float32       |
|  Current Avg                       | A                     | Float32       |
|  Voltage L1-L2                     | V                     | Float32       |
|  Voltage L2-L3                     | V                     | Float32       |
|  Voltage L3-L1                     | V                     | Float32       |
|  Voltage L-L Avg                   | V                     | Float32       |
|  Voltage L1-N                      | V                     | Float32       |
|  Voltage L2-N                      | V                     | Float32       |
|  Voltage L3-N                      | V                     | Float32       |
|  Voltage L-N Avg                   | V                     | Float32       |
|  Active power phase 1              | kW                    | Float32       |
|  Active power phase 2              | kW                    | Float32       |
|  Active power phase 3              | kW                    | Float32       |
|  Total active power                | kW                    | Float32       |
|  Power factor total                | -                     | Float32       |
|  Frequency                         | Hz                    | Float32       |
|  Total active energy import        | Wh                    | Int64         |

## Install the App

*powerlogic-edge* comes with pre-builded ```powerlogic-edge_x.x.x.app``` package that can be installed specifically on Unified Comfort Panels that runs SIMATIC Edge Runtime.

### Download the App

The **powerlogic-edge** app can be downloaded in .app format from this repository [powerlogic-edge_x.x.x.app](https://drive.google.com/drive/folders/150FJPrJYlrYPZrD2MwN5WK9AnhwfODJG)

### Prerequisites

1. A Unified Comfort Panel with SIMATIC Edge feature enabled.
2. At least one user needs to be signed up

### Load App on Unified Comfort Panels

1. Copy the downloaded ```powerlogic-edge_x.x.x.app``` file to your Developer PC.
2. Open the Industrial Edge Management Web Page of UCP on ```https://<ucp-address>```
3. Import the .app file using the *Import Offline* button
4. Wait until App is installed

## WinCC Unified Configuration

In order for the application to work, it is necessary to insert some elements inside your WinCC Unified project, including :

- **"EdgePowerLogicTags"** Table Variables;

These elements are included in a TIA Portal V17 library **"EdgePowerLogicLibrary"** provided along with the powerlogic-edge application and an application example.

### "EdgePowerLogicLibrary" Library Import

From the TIA Portal V17 engineering software, open the **"Library"** side menu.
Use the **"Open Global Libraries"** button and import the ```EdgePowerLogicLibrary.zal17``` file.

### Table "EdgePowerLogicTags" variables

Import the **"EdgePowerLogicTags"** Tags table within the HMI Tags of your TIA Portal V17 project.

Below are the details of the HMI Tags of the **"EdgeReportTags"** variable table:
| HMI Tag Name                       | Type                  | Description                        | 
| ---------------------------------- | --------------------- | ---------------------------------- | 
|  I1                                | Real                  | Phase current 1 (A)                |
|  I2                                | Real                  | Phase current 2 (A)                |
|  I3                                | Real                  | Phase current 3 (A)                |
|  I_Avg                             | Real                  | Current Avg (A)                    |
|  L1_L2                             | Real                  | Voltage L1-L2 (V)                  |
|  L2_L3                             | Real                  | Voltage L2-L3 (V)                  |
|  L3_L1                             | Real                  | Voltage L3-L1 (V)                  |
|  LL_Avg                            | Real                  | Voltage L-L Avg (V)                |
|  L1_N                              | Real                  | Voltage L1-N (V)                   |
|  L2_N                              | Real                  | Voltage L2-N (V)                   |
|  LN_Avg                            | Real                  | Voltage L-N Avg (V)                |
|  Active_Power_Ph1                  | Real                  | Active power phase 1 (Kw)          |
|  Active_Power_Ph2                  | Real                  | Active power phase 2 (Kw)          |
|  Active_Power_Ph3                  | Real                  | Active power phase 3 (Kw)          |
|  Active_Power_Tot                  | Real                  | Total active power (Kw)            |
|  Power_Factor                      | Real                  | Power factor total                 |
|  Frequency                         | Real                  | Frequency (Hz)                     |
|  Total_Active_Energy_Imported      | LReal                 | Total active energy imported (KwH) |
|  Ip_Address                        | WString               | Multimeter IPv4 address            |
|  Port_Number                       | WString               | Multimeter Modbus port             |
|  Unit_Id                           | Int                   | Multimeter Modbus unit ID          |
|  Enable                            | Bool                  | Enable application                 |
|  Connection_State                  | Int                   | **0**: disconnected; **1**: connecting; **2**: connected |

## How to use
In order for the application to work, the following steps must be followed:
- Start **powerlogic-edge** from *Edge Management* 
- Set *PowerLogic* communication parameters
- Enable application with *Enable* switch
- Connect variables for energy measures visualization


![powerlogic-config](EdgePowerLogicSettings.png)


## Release History

- 0.0.1
  - The first release.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contributing

1. Fork it ([https://github.com/yourname/yourproject/fork](https://github.com/yourname/yourproject/fork))
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

## Contacts

- Nicolò Toscani - [toscani.nicolo90@gmail.com](toscani.nicolo90@gmail.com)


