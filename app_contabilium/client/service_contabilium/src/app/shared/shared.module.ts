import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { SpinnerComponent } from './spinner/spinner.component';
import { NavBarComponentComponent } from './nav-bar-component/nav-bar-component.component';
import { RouterModule } from '@angular/router';
import { MaterialModule } from '../material/material.module';
import { LogInDialogComponent } from './nav-bar-component/log-in-dialog/log-in-dialog.component';
import { ReactiveFormsModule } from '@angular/forms';
import { NavItems } from './nav-items/nav-items';
// import {
//   MatInputModule, MatPaginatorModule, MatProgressSpinnerModule,
//   MatSortModule, MatTableModule, MatDatepickerModule, MatNativeDateModule,
//   MatIconModule, MatButtonModule, MatProgressBarModule, MatToolbarModule, MatFormFieldModule, MatSelectModule, MatDividerModule, MatCardModule, MatRadioModule
// } from "@angular/material";

@NgModule({
  imports: [
    CommonModule,
    RouterModule.forRoot([]),
    MaterialModule,
    ReactiveFormsModule,
  ],
  declarations: [SpinnerComponent, NavBarComponentComponent, LogInDialogComponent],
  exports: [
    SpinnerComponent
  ],
  providers: [
    NavItems
  ]
})
export class SharedModule { }
