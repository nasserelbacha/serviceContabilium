import { Injectable } from "@angular/core";
import {
  HttpRequest,
  HttpHandler,
  HttpEvent,
  HttpInterceptor,
} from "@angular/common/http";
import { Observable, throwError } from "rxjs";
import { catchError } from "rxjs/operators";
import { Component, OnInit, Inject, ChangeDetectorRef } from "@angular/core";
import {
  MatDialog,
  MatDialogRef,
  MAT_DIALOG_DATA,
} from "@angular/material/dialog";

import { ErrorExceptionService } from "src/app/services/errorexception.service";
import { Router } from "@angular/router";
import { environment } from "../../../environments/environment";
import { SnackbarService } from "../../services/snackbar.service";


@Injectable()
export class ErrorInterceptor implements HttpInterceptor {
  constructor(
    public dialog: MatDialog,
    public errMsg: ErrorExceptionService,
    public router: Router,
    public snackBar: SnackbarService,
  ) {}

  errorException = this.errMsg.getHandledExceptions();
  blackListedUrl = "";

  intercept(
    request: HttpRequest<any>,
    next: HttpHandler
  ): Observable<HttpEvent<any>> {
    let cutmsg : any;

    return next.handle(request).pipe(
      catchError((err) => {
        console.log(err)
        const msg =
          !err || !err.error || !err.error.message ? "" : err.error.message;

        if (err.error) {
          cutmsg = err.error[0]
        }
        if (!cutmsg) {
          cutmsg = "";
        }

        let found = this.errorException.find((elem) => cutmsg.includes(elem));

        if (found) {
          console.log(cutmsg)
          throw Error(cutmsg)
          // return throwError(() => {cutmsg});
        }

        const noExcepTime : any = localStorage.getItem("noExceptions");
        if (+noExcepTime > new Date().getTime()) {
          return throwError(() => cutmsg);
        } else {
          // snackbar executed una vez
          this.snackBar.error("error");

          // errordialog executed muchas veces pero con closeall
          // const dialogRef = this.dialog.open(ErrorDialog, {
          //   width: "500px",
          //   disableClose: false,
          //   data: err,
          // });

          const error = (err.error ? err.error.message : "") || err.statusText;
          return throwError(() => error);
        }
      })
    );
  }
}

@Component({
  selector: "error.dialog",
  templateUrl: "error.dialog.html",
  styleUrls: ["error.dialog.css"],
})
export class ErrorDialog {
  text = "";

  constructor(
    public dialogRef: MatDialogRef<ErrorDialog>,
    @Inject(MAT_DIALOG_DATA) public data : any,
    public errMsg: ErrorExceptionService,
    public dialog: MatDialog
  ) {
    this.text = JSON.stringify(data);
  }

  onNoClick(): void {
    this.dialogRef.close();
    this.dialog.closeAll();
  }

  startTimer() {
    localStorage.setItem("noExceptions", new Date().getTime() + 30 * 1000 + "");
    this.dialogRef.close();
    this.dialog.closeAll();
  }
}
