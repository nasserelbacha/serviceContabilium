import { Component, OnInit } from '@angular/core';
import { MatDialogRef } from '@angular/material/dialog';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { AuthService } from 'src/app/services/auth.service';
import { CompanyLoginBody } from '../../../helpers/clases/companyLoginBody';
import { Router } from '@angular/router';
import { throwError } from 'rxjs';

@Component({
  selector: 'app-log-in-dialog',
  templateUrl: './log-in-dialog.component.html',
  styleUrls: ['./log-in-dialog.component.css']
})
export class LogInDialogComponent implements OnInit {

  constructor(
    private dialogRef : MatDialogRef<LogInDialogComponent>,
    private formBuilder: FormBuilder,
    private authService : AuthService,
    private router : Router
  ) { }

  loginForm: FormGroup;
  error: any = "";
  submitted : boolean = false;
  loading : boolean = false

  get form() {return this.loginForm.controls;}

  ngOnInit(): void {
    this.loginForm = this.formBuilder.group({
      companyEmail: ['', Validators.required],
      companyPassword: ['', Validators.required]
    })
  }

  close(){
    this.dialogRef.close()
  }

  async onSubmit(){
    this.submitted = true
    localStorage.clear()
    if(this.loginForm.invalid){
      return;
    }
      this.loading = true
        const body : CompanyLoginBody = {
          email : this.form['companyEmail'].value,
          password : this.form['companyPassword'].value
        }
        this.authService.authCompany(body)
        .subscribe(async (res)  => {
          console.log(res)
          await localStorage.setItem('token', res.jwt);
          await localStorage.setItem('role', res.role);
          const user = this.authService.parseJwt(res.jwt);
          localStorage.setItem('user', JSON.stringify(user));
          this.router.navigate(['invoices/load-invoice']);
          this.dialogRef.close();
      }, error => {
        this.loading = false
        this.error = error
      })
  
    }
}
