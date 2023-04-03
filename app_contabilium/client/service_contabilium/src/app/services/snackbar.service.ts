import { Injectable } from "@angular/core";
import { MatSnackBar } from "@angular/material/snack-bar";
import { ErrorDialog } from "../helpers/interceptor/error.interceptor";

@Injectable({ providedIn: "root" })
export class SnackbarService {
  openFromComponent(ErrorDialog: ErrorDialog) {
    throw new Error('Method not implemented.');
  }
  constructor(private snackbar: MatSnackBar) {}


  open(title : string, duration : number, type : string) {
    this.snackbar.open(title, "✓", {
      duration: duration,
      horizontalPosition: "end",
      verticalPosition: "top",
      panelClass: ["mat-snack-" + type],
    });
  }

  deletedOK() {
    this.open("borrar", 4000, "success");
  }

  error(text: string) {
    this.open(text, 4000, "error");
  }

  ok(text : string) {
    this.open(text, 4000, "success");
  }
}
