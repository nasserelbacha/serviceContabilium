import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { AppConfig } from '../_AppConfig/app-config';

@Injectable({
  providedIn: 'root'
})
export class ProviderService {

  constructor(
    private httpClient : HttpClient
  ) { }

  getProvidersByCompany(){
    const user = JSON.parse(localStorage.getItem('user') || '{}')
    return this.httpClient.get<any>(AppConfig.COMPANIES + "/" + user.company.id + "/providers")
  }
}
