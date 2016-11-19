/* tslint:disable:no-unused-variable */

import { TestBed, async, inject } from '@angular/core/testing';
import { GenieService } from './genie.service';

describe('Service: Genie', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [GenieService]
    });
  });

  it('should ...', inject([GenieService], (service: GenieService) => {
    expect(service).toBeTruthy();
  }));
});
