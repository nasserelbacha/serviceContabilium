import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  {path:"", redirectTo:"dashboard/user", pathMatch: "full"},
  {
    path: '',
    children: [{
      path: 'dashboard',
      loadChildren: () => import('./pages/dashboard/dashboard.module').then(m => m.DashboardModule)
    }]
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

