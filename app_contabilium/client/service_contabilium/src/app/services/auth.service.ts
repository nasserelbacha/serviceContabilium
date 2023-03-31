import { HttpClient, HttpResponse } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { CookieService } from 'ngx-cookie-service';
import { throwError } from 'rxjs';
import { CompanyLoginBody } from '../helpers/clases/companyLoginBody';

import { AppConfig } from '../_AppConfig/app-config';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor(
    private httpClient : HttpClient,
    private cookieService : CookieService,
    private router:Router,
  ) { }

  private _token :string | null;
  private _role: string | null;

    authCompany(body: CompanyLoginBody){
      return this.httpClient.post<any>(AppConfig.AUTH_COMPANY, body)
    }
    
    isNotAuthorized(e : any): boolean {
      if(e.status==401){
        if(this.isAuthenticated()){
          this.logOut();
        }
        this.redirectLogin();
        return true;
      }

      if(e.status==403){
        this.router.navigate(['/']);
        return true;
      }

      return false;
    }

    isAuthenticated(): boolean{
      return this.getToken() != null
    }

    public getToken(){
      const data = this._token
      if(!data){
        return null
      }
      return data
    }

    parseJwt (token: string) {
      var base64Url = token.split('.')[1];
      var base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
      var jsonPayload = decodeURIComponent(window.atob(base64).split('').map(function(c) {
          return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
      }).join(''));
  
      return JSON.parse(jsonPayload);
    }

    logOut(){
      this.httpClient.post<any>(AppConfig.API_ENDPOINT + "/logout", {}).subscribe(async () => {
        localStorage.removeItem('token')
        localStorage.removeItem('user')
        localStorage.removeItem('role')
        window.location.reload()
        // this.cookieService.delete('jwt')
        // this.cookieService.delete('role')
      })
    }

    public get token(): string | null{
      if(this._token!=null){
        return this._token;
      } else if(this._token==null && localStorage.getItem('token')!=null){
        this._token = localStorage.getItem('token');
        return this._token;
      }
      return null;
    }

    public get role(): string | null{
      if(this._role!=null){
        return this._role
      }
      else if(this._role==null && localStorage.getItem('role')!=null){
        this._role = localStorage.getItem('role')
      } 
      return null;
    }

    redirectLogin(){
      this.router.navigate(['dashboard/user']);
    }
}
