

var socket = new Websocket("ws://localhost:8000/ws-connect/");
socket.onmessage = function(e){

	var djangoData = JSON.parse(e.data);
	console.log(djangData);

	document.querySelector("#app").innerText = djangoData.value;

}