<h2>Wiring</h2>

<h3>RC522</h3>

<table>
<thead>
<tr>
<th>RC522 pin name</th>
<th>RPi pin name</th>
</tr>
</thead>
<tbody>
<tr>
<td>SDA</td>
<td>GPIO8, CE0</td>
</tr>
<tr>
<td>SCK</td>
<td>GPIO11, SCKL</td>
</tr>
<tr>
<td>MOSI</td>
<td>GPIO10, MOSI</td>
</tr>
<tr>
<td>MISO</td>
<td>GPIO9, MISO</td>
</tr>
<tr>
<td>IRQ</td>
<td>GPIO24</td>
</tr>
<tr>
<td>GND</td>
<td>Ground</td>
</tr>
<tr>
<td>RST</td>
<td>GPIO25</td>
</tr>
<tr>
<td>3.3V</td>
<td>3V3</td>
</tr>
</tbody>
</table>

<br>
<h3>Button</h3>

<br><p><strong>Check this section for accuracy!!! ---V</strong></p><br>

<table>
<thead>
<tr>
<th>Button pin name</th>
<th>RPi pin name</th>
</tr>
</thead>
<tbody>
<tr>
<td>Eject Button</td>
<td>GPIOX, 220ohm Pullup</td>

</tr>
<tr>
<td>GND</td>
<td>GND</td>
</tr>
</tbody>
</table>

<br>
<h3>SG-90 Servo</h3>

<table>
<thead>
<tr>
<th>Button pin name</th>
<th>RPi pin name</th>
</tr>
</thead>
<tbody>
<tr>
<td>Red<sup>5V</sup</td>
<td>5V</td>
</tr>
<tr>
<td>Black<sup>GND</sup></td>
<td>GND</td>
</tr>
<tr>
<td>Orange<sup>PWM</sup></td>
<td>GPIOX</td>
</tr>
</tbody>
</table>

<h2>Printing the Case</h2>

<h2>Assembly</h2>


<h2>Software</h2>
    <p>The software is built in python and running on top of Raspbian Linux in a light, terminal-only configuration. It reads cards using the pi-rc522 library. From there depending on the information stored the local {table databace}-Replace will ouput a code that the Spotipy library will ask spotify to play on specified device. While this is happening, the Raspberry Pi is also repeatedly checking to see if the [EJECT] button is pressed. If the button is being pressed, the pigpio library will control the servo to eject the disk. </p>

[Link to RC-552 GitHub](https://github.com/ondryaso/pi-rc522)
<br>
[Link to Spotipy Docs](https://spotipy.readthedocs.io/en/)
<br>
[Link to pigpio GitHub](https://github.com/fivdi/pigpio#servo-control)

## API Reference

> **\_\_init__** *( credentialsDirectory = None, scope = 'user-read-private user-read-playback-state user-modify-playback-state', debugStatus = 1, connect = True, platform = "PI" )*

Creates a PSL client. Will automaticly call *loadCredentials*.

<br>

**Parameters:**

* **credentialsDirectory** - The path to the .csv file that contains the credentials required for login into the spotify system.

* **scope** - The scope or "amount of privileges" that are being request from spotify for the specified account.

* **debugStatus** - The verbosity of the debug console. The number inputed can range from 0 (no verbosity) to 3 (full verbosity).

* **connect** - The option to turn on/off the *self.connect* internal function that submits the credentials to spotify.

* **platform** - The platform that PSL is running for. The "PC" option disables the iporting of libraries specific to the raspberry pi.

<br>
<br>

> **loadCredentials** *( directory = None )*

Will automaticly read credentials from *directory* stored as a .csv and assigns credentail class variables. Automaticly called by the *\_\_init__* function.

<br>

**Parameters:**

* **directory** - The path to the .csv file that contains the credentials required for login into the spotify system.

<br>
<br>

> **load** *( )*

Will automaticly read credentials from *self.libraryDirectory* (set by *loadCredentials*) stored as a .csv and assigns the directory class variable.
<br>

**Parameters:**

* **None** - None.

<br>
<br>

> **save** *( )*

Will automaticly save credentials to *self.libraryDirectory* (set by *loadCredentials*) stored as a .csv.
<br>

**Parameters:**

* **None** - None.

<br>
<br>

> **connect** *( )*

Use the defined credentials to establish a connection to spotify.
<br>

**Parameters:**

* **None** - None.

<br>
<br>

> **read** *( )*

Will read what is currently on the nfc sensor (in the card slot) and return the *Unique Identification (UID)* or None.
<br>

**Parameters:**

* **None** - None.

<br>
<br>

> **play** *( uri = None )*

Will play the given URI on the connected spotify device.
<br>

**Parameters:**

* **uri** - The *Unique Identification (UID)* that is wished to be played.

<br>
<br>

> **eject** *( )*

Will actuate the servo to eject the disk that is currently installed into the PSL.
<br>

**Parameters:**

* **None** - None.

<br>
<br>

> **cleanUp** *( )*

Will cleanup the *gpio* an *rfid* connections. 
<br>

**Parameters:**

* **None** - None.

<br>
<br>

> **debugMessage** *( verbosityLevel = None, message = None )*

Will display a message if the verbosity level is equal to or bigger than the specified number.
<br>

**Parameters:**

* **verbosityLevel** - The level that the message will be displayed at.

* **message** - The message to notify the user.

<br>

<h2>Use</h2>