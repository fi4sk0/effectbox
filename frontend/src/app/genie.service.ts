import { Injectable, OnInit } from '@angular/core';

@Injectable()
export class GenieService {

  constructor() { }

  ws = new WebSocket("ws://rpi3:8765")
  
  EFFECTS = {"noise": {"description": "Super noisy effect"}};

  getEffects(): any {

    var my_websocket = this.ws

    my_websocket.onopen = (event) => {
      console.log("Sending query")
      my_websocket.send("query")
    }


    var promise = new Promise(function(resolve, reject) {
      my_websocket.onmessage = (message) => {      
        resolve(JSON.parse(message.data))
      }
    });

    return promise
  }

  sendConfiguration(config) {
    this.ws.send(config)
  }

}
