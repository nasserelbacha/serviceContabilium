import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { AppConfig } from '../_AppConfig/app-config';

@Injectable({
  providedIn: 'root'
})
export class TestService {

  constructor(
    private httpClient : HttpClient
  ) { }

  test(){
    return this.httpClient.get<any>(AppConfig.COMPANIES)
  }
}
