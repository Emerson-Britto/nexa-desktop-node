const { io } = require("socket.io-client");
const prompt = require('prompt-sync')();


const socket = io(`http://127.0.0.1:3080/a/desktop`);

socket.on("connect", () => {
  console.log("connected to Nexa Server");
});

console.log("I need a Room Key. You can request it to me on telegram");
const connect_to_room = () => {
  const connection_key = prompt("Room Key: ");
  if (!connection_key) return
  socket.emit("connect_to_room", connection_key);  
}

connect_to_room()

socket.on("connected_to_room", res => {
  console.log(`${res.msg} (status: ${res.status})`);
})

socket.on("room_key_error", res => {
  console.log(`${res.msg} (status: ${res.status})`);
  console.log("sorry, try again.");
  connect_to_room();
})
