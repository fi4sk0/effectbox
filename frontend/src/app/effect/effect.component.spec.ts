/* tslint:disable:no-unused-variable */
import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { By } from '@angular/platform-browser';
import { DebugElement } from '@angular/core';

import { EffectComponent } from './effect.component';

describe('EffectComponent', () => {
  let component: EffectComponent;
  let fixture: ComponentFixture<EffectComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ EffectComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(EffectComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
