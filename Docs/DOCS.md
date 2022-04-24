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

<h2>Use</h2>