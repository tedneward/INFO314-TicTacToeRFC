# TicTacToeRFC
An [RFC](RFC.md) for a protocol for playing a game of TicTacToe over the network

## Goals

Your job is to implement "RFC INFO314", also known as TTTP, or the "Tic Tac Toe Protocol". This protocol is defined [here](RFC.md), and will serve as the sole description of the protocol--neither your instructor nor the TA will answer any questions about the protocol. *It is up to you to implement the protocol as defined in the specification, and where any incompatibilities arise, work those out with other groups on your own.*

## Rubric (25 pts)

The grade for this project is broken out across several parts: writing a console-UI client, writing the server, demonstrating that your client and server can interoperate with other groups' client and server, and presenting your solution to the rest of the class during Finals.

### Write a TTTP Client (5pts)

* create a console UI client that can:
    * start a game
    * display the state of the board
    * make a move on the board
    * plays through to game termination
    * starts a second game
* communicates over either TCP or UDP
* provides console output about communication
    * also known as "diagnostic logging"

Be sure to allow for the client to play over either TCP or UDP, either by accepting a command-line parameter or asking via some kind of interactive prompt.

### Write a TTTP Server (5pts)

* create a server that can:
    * accept requests from multiple clients
    * start a game
    * validate player moves
    * plays through to game termination
* manages up to 10 clients simultaneously
* accepts communication over TCP or UDP
* provides console output about communication (diagnostic logging)

Diagnostic logging levels should be able to be dynamically configured via a command-line parameter or configuration file, and any changes in configuration take place on restart.

### Cross-group interoperability (10 pts)

* run your client against another group's server (5pts)
* run another group's client against your server (5pts)
* create a recording of a Zoom call doing so
* play at least two games to completion on the recording

Note that the groups interoperated with must be different--in other words, group "A" uses their client against group "B"'s server, but must find a group "C" with which to test "A"'s server. (This is to avoid any sort of odd-group-out scenarios where groups all pair off and one group is left with no one to interoperate with.)

### Present! (5 pts)

* During our finals time, present to the class
* Describe your implementation
* Which groups did you interop with? How was that?
* What was one thing that was easier than you expected?
* What was one thing that was harder than you expected?

At least one member of the group must be present during Finals for this.

## Extra credit
There are several opportunities to earn some extra credit points as a group on this assignment.

### Be the standard! (2 pts)

* Show a video of three groups interoperating:
    * client A, client B, and server C
* Maximum of three "triplets" (6 pts max)

In other words, coordinate and demonstrate interoperability three ways simultaneously: one group starts up a server, the second group starts up their client, the third group starts up their client, and groups 2 and 3 play a game against one another.

### Improve the RFC (5pts)

* propose extensions to the protocol:
    * asymmetrical board size (3x5, 5x3, etc)
    * multiple players (3-, 4-players)
* must be written in the form of the RFC
    * create a file called RFC-Proposed.md in your repo directory
    * add the text describing your extension
* implement your extension
    * extend your client and server
    * *make sure you version-negotiate correctly*
* demonstrate that your client works with your server
    * must show off the extension
* demonstrate that your implementations work with non-extended versions

This can be included in any of the previous videos, but be sure to demonstrate *both* the expected (v1) functionality as well as your extended functionality.

### Implement useful clients (2 pts each)

* Implement a "announcer" client
    * connects to a server and "watches" games w/o making moves
    * provides information about changes in game status
* Implement an "AI" client
    * connects to a server, plays a game with another player
    * your AI need not be good!

We will consider proposals for other useful clients as well! Just please propose the new client type *before* submission, so that we have a chance to redirect efforts that would be less-than-useful (or interesting) before you do all the work on it.
