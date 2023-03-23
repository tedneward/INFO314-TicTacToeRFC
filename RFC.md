# RFC INFO314

## Abstract
This RFC details a network protocol for two players to play a game of Tic-Tac-Toe over a computer network.

## Status of This Memo
This document is not an Internet Standards Track specification; it is published for informational purposes, primarily for the purpose of students taking my INFO314 class at the University of Washington, Seattle to implement a protocol from RFC and hopefully have a little fun doing it. Hosts on the ARPA Internet that choose to implement a Tic Tac Toe Protocol service are expected to adopt and implement this standard.

This document is not a product of the Internet Engineering Task Force (IETF) and does not in any way represents the consensus of the IETF community. It has received almost no public review, has not been approved for publication by the Internet Engineering Steering Group (IESG), and probably should not be used for production purposes by anyone.

Information about the current status of this document, any errata, and how to provide feedback on it may be obtained at https://github.com/tedneward/TicTacToeRFC. 

## Copyright Notice
There is no copyright associated with this document, and anyone is free to use it for whatever purposes they find useful. However, this document also carries with it no assertions or promises, implied or explicit, as to the accuracy or correctness of any statement found herein. In short, this document should not be used for anything important, ever.

## Table of Contents

1. [Status of this memo](#status-of-this-memo)
2. [History](#history)
3. [Rules of Tic-Tac-Toe](#rules-of-tic-tac-toe)
4. [Detailed Description](#detailed-description)
    1. [Description of terms](#description-of-terms)
    2. [TCP Based Service](#tcp-based-tic-tac-toe-service)
    3. [UDP Based Service](#udp-based-tic-tac-toe-service)
5. [References](#references)

## History
An early variation of the game was played in the Roman Empire, around the 1st century B.C. It was called "terni lapilli," which means "three pebbles at a time." The game's grid markings have been found chalked all over Roman ruins. Evidence of the game was also found in ancient Egyptian ruins.

The first print reference to "noughts and crosses," the British name for the game, appeared in 1864. The first print reference to a game called "tick-tack-toe" occurred in 1884 but referred to a children's game played on a slate.

## Rules of Tic-Tac-Toe
The game of Tic-Tac-Toe, also known as "Naughts and Crosses", is played between two players on a 3x3 square grid. The goal is for each player to create a contiguous straight (in a row) placement of three of their tokens (labeled either "X" or "O") on the grid. Players alternate turns placing a token on the grid in one of the nine spaces.

### Determination of which player begins
Various means are used to determine which player plays first: a coin flip is common, although other means are also common. In some cases, players may agree to allow the player losing the previous game to go first, since going first is commonly considered to be an advantage in the game.

### Restrictions around token placement
Players may place their token in any unoccupied square; that is, they may not place a token in a square occupied by an opponent.

### Game termination
The game is over as soon as one player has achieved three-in-a-row; not of the grid need be filled.

If all nine squares are filled and no player has three-in-a-row, the game is a stalemate (also sometimes called a "cats" game, for reasons lost to history), and no winner is declared.

## Detailed Description
The following describes the expectations of both client and server in the Tic-Tac-Toe Protocol (abbreviated "TTTP" in places where the full name would be unwieldy).

### Description of terms
This protocol assumes the existence of a process running on a network that acts as the primary arbiter of the process of playing the game; this process is called the "server", and is referred to as such in this document. Similarly, processes that represent the players of the games are referred to as "clients". Note that this document makes no prescriptive judgment as to whether the "server" and "client" are separate processes; it is entirely feasible for one process to serve as both "client" and "server" simultaneously, at least for one client.

Clients interact with the server in uniquely-identifed "sessions". These are indentified by unique strings of non-whitespace ASCII characters and are called "session identifiers". The server is permitted complete freedom in how it generates session identifiers, save that they must be unique at any time, and cannot exceed 80 characters in length.

Clients play each other in games that are also uniquely-identified. These "game identifiers" are similar to session identifiers in that they are strings of non-whitespace ASCII characters that cannot exceed 80 characters in length.

### TCP Based Tic Tac Toe Service

A Tic-Tac-Toe service is defined as a connection based application on TCP listening for TCP connections on TCP port 3116[1](#1). Once a [connection is established](#session) a Tic Tac Toe session is considered to have started and remains in an "alive" state until either the client or the server chooses to [close the session](). In the TCP session, either client or server may initiate the sending of messages in a fully-duplexed fashion.

### UDP Based Tic Tac Toe Service

Another Tic-Tac-Toe service is defined as a datagram based application on UDP listening for UDP datagrams on UDP port 3116[1](#1). When a datagram is received, a Tic Tac Toe session is considered to have started, and remains in an "alive" state until either the client or server [sends a "close" message](#gdby) or the server [has not heard from the client over a period of time](). All datagram communication occurs over port 3116.

### Session
A client must connect with a server before any game can be created. This is called "establishing a session" and requires the client to send a [greeting message]() to the server, self-identifying the client with a unique string to be used as part of the protocol later. Once the client has identified, the server [acknowledges](#sess) receipt, including a "session identifier" which uniquely identifies this session.

The server is permitted to use any sort of scheme for session identifiers, so long as they do not include whitespace. Thus, values of "1234" (integer values), "0cb8d694-3999-4bc6-8351-0e978b62a08d" (GUIDs), or "57.34" (floating point values) would all be acceptable. Some servers may choose the floating-point scheme to allow sessions to indicate relationships to one another; for example, two players may be in sessions "4.1" and "4.2", respectively, with observers on sessions "4.3" and "4.4". However, each of these sessions is considered unique, has no special relationship to one another, and is purely left as a server implementation detail.

### Creating a game
A client can choose to create a new game (in essence looking for another player) by sending a [create](#crea) message to the server. This will create a new, unique game on the server that is still missing a player, and the server will respond with a [joined-game](#join) message; this is the same response as if the client [joined](#join) an existing game. Since there is no second player yet in this game, the client will receive no further messages from the server until a (different) client joins the game.

### Finding a game
A client can also ask to see a list of open games on the server by sending a [game list]() message to the server. The server will respond with a [list of open games](). From there, the client can select a game and ask to join it.

### Joining a game
A client can ask to join an open game by sending a [join](#join) message to the server.

Assuming the game is now filled with its minimum number of players, the server will respond with a message to all clients indicating whose move (referenced by client identifier) is first. That player will be given the moniker "X".

### Making a move
A client can make a move on its 

### Getting game status
A client can request a complete status of the game by sending a [game status]() message

### Timeout
In the event that the server has not received a message from either of its player clients in a configurable period of time, the server is free to send a [close]() message to 

## Message Reference
Messages sent in this protocol consist of a 4-letter ASCII command phrase, with additional information following until a CRLF terminator.

### CREA
Sent by a client to the server to create a new game. This client is assumed to be one of the players. The server should respond with a [join](#join) message.

### GDBY
Sent by either the client or the server to its counterpart to indicate it is finished with the session. If this is a client who is sending the message, it is assumed to implicitly be sending a [quit](#quit) message to the game(s) in which it is a player.

### HELO
Sent by a client to a server to initiate a session with the server. The command is expected to include the version of the protocol understood by the client, and an identifier by which the client identifies itself--an email address for a human, for example, or a GUID for an autonomous agent. Examples: `HELO 1 ted@tedneward.com` or `HELO 1 0cb8d694-3999-4bc6-8351-0e978b62a08d`. The server is expected to respond with a [session initiation]() command.

### JOIN
Sent by the server to the client to indicate the client has successfully joined the game. The message will include the JOIN command, and the game identifier.

### MOVE

### STAT
This message expects a game-identifier body, indicating the game whose status is requested.

### TERM
This message indicates the termination of a game. The message includes the game-identifier, and the client-identifier of the player who is declared the winner. For games which are stalemate, no client-identifier is sent after the game-identifier.

### QUIT
Sent by the client to indicate that the player wishes to abandon the game without terminating the session. The QUIT message is expected to include the game identifier of the game being quit. The player opposite the quitting player is immediately declared the winner of the game, and the game is considered to be concluded/finished.

### SESS
This is sent by the server to the client to indicate the server has officially created a unique session between it and the client. The command is expected to include the version of the protocol the server will use with the client, and the unique session identifier itself. These values will be separated by whitespace. Examples: `SESS 1 57` or `SESS 1 0cb8d694-3999-4bc6-8351-0e978b62a08d`.

### YRMV
This message is sent by the server to al of the participant clients in a game to indicate which player's move is currently accepted. This message always includes the command, the game identifier, and the client identifier whose move is currently accepted. Once this message is sent, the server will not accept any [move]() commands from a client other than the one whose identifier was included in this message.

## Footnotes

### 1
This port is chosen because it is the combination of "3" and "116", the ASCII code for the character "t"; in short, "3t", referencing the name starts with three simultaneous "t" characters.

## References

* https://www.exploratorium.edu/brain_explorer/tictactoe.html

* https://www.thesprucecrafts.com/tic-tac-toe-game-rules-412170
