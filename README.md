# Python WebSocket Chat Application

## What are WebSockets?

WebSockets are a communication protocol that provides full-duplex, real-time communication channels over a single TCP connection. Unlike traditional HTTP requests, WebSockets allow for bi-directional, event-driven communication between a client (typically a web browser) and a server.

## What do WebSockets do?

WebSockets enable:
- Real-time, bi-directional communication
- Persistent connections between client and server
- Low-latency data transfer
- Server-initiated communication to the client

## Use Cases for WebSockets

WebSockets are particularly useful for applications that require real-time updates or frequent communication between client and server. Some common use cases include:

1. Chat applications
2. Live sports updates or stock tickers
3. Online gaming
4. Collaborative editing tools
5. Real-time data visualization
6. IoT device communication

## Our Reference Implementation

This project implements a simple real-time chat application using Python and the `websockets` library. It consists of two main components:

1. A WebSocket server that handles multiple client connections and broadcasts messages.
2. A WebSocket client that can send and receive messages.

### Features

- Multiple clients can connect to the server simultaneously
- Messages sent by one client are broadcast to all other connected clients
- Simple command-line interface for sending and receiving messages

## How to Use

### Prerequisites

Ensure you have Python 3.7 or later installed on your system.

### Installation

1. Clone this repository or download the source files.
2. Install the required dependencies:

```bash
pip install websockets aioconsole asyncio
```

### Running the Application

1. Start the server:
   ```bash
   python server.py
   ```
   The server will start running on `localhost:8765`.

2. In separate terminal windows, run the client for each user:
   ```bash
   python client.py
   ```

3. Once connected, you can type messages in the client terminal. Press Enter to send a message.

4. Messages will be broadcast to all connected clients.

### Testing

To test the application:

1. Run the server in one terminal window.
2. Run multiple instances of the client in separate terminal windows.
3. Type messages in each client window and observe that they are received by all other clients.

## Next Steps

This is a basic implementation that can be extended with features such as:

- User authentication
- Private messaging
- Persistent chat history
- Web-based front-end
- Message encryption