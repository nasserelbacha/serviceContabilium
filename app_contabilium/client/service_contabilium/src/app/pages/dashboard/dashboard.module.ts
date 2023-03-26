import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { DashBoardRoutingModule } from './dashboard-routing.module';
import { DashboardViewComponent } from './dashboard-view/dashboard-view.component';


@NgModule({
  imports: [
    CommonModule,
    DashBoardRoutingModule
  ],
  declarations: [DashboardViewComponent],
})
export class DashboardModule { }
