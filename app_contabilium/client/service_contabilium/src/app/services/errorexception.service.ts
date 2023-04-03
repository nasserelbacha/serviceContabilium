import { Injectable } from '@angular/core';

const exceptions = [
"Change Password Error. There were errors provided. Please check your input.. ",
"Bad credentials",
"doesn't have access to requested resource.",
"Invalid Token",
"already exists!",
"User already has an account, please use login section.",
"Account not found, please use Register account section.",
"Invalid Confirmation Token Or Email",
"incorrect password"
]

@Injectable({
providedIn: 'root'
})
  
export class ErrorExceptionService {

    getHandledExceptions(){
      return exceptions
    }

}