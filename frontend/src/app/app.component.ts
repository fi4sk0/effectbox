import { Component, OnInit} from '@angular/core';
import { GenieService } from './genie.service'
import { EffectComponent } from './effect/effect.component'

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [GenieService]
})

export class AppComponent {
  title = 'Genie App';

  effects = {}
  effectNames:String[]

  constructor(private genieService: GenieService) { }

  ngOnInit() {
    console.log("Getting effects")
    this.genieService.getEffects().then(effects => {
      this.effectNames = Object.keys(effects)
      this.effects = effects
    })
  }

  dataChanged(data, name) {

    var configuration = {}
    configuration[name] = {"parameters": data}
    
    this.genieService.sendConfiguration(JSON.stringify(configuration))
  }
}
