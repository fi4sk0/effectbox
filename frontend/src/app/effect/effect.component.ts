import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { GenieService } from '../genie.service'
@Component({
  selector: 'effect',
  templateUrl: './effect.component.html',
  styleUrls: ['./effect.component.css'],
  providers: [GenieService]
})
export class EffectComponent implements OnInit {

  constructor(private genieServer: GenieService) { }

  @Input()
  data: any

  @Output()
  dataChange = new EventEmitter()

  parameterNames: String[]

  ngOnInit() {
    console.log(this.data)
    this.parameterNames = Object.keys(this.data.parameters)
    console.log(this.parameterNames)
  }

  changed(value, name) {
    this.data.parameters[name].value = value
    console.log(this.data)
    var data = {}
    data[name] = {"value": +value}

    this.dataChange.emit(data)
  }
}
