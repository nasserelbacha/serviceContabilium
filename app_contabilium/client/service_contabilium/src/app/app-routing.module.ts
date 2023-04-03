import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AuthGuard } from './helpers/guards/auth.guard';
import { LoginGuard } from './helpers/guards/login.guard';
import { NavBarComponentComponent } from './shared/nav-bar-component/nav-bar-component.component';

const routes: Routes = [
  {path:"", redirectTo:"dashboard/user", pathMatch: "full"},
  {
    path: '',
    component: NavBarComponentComponent,
    children: [{
      canActivate: [LoginGuard],
      path: 'dashboard',
      loadChildren: () => import('./pages/dashboard/dashboard.module').then(m => m.DashboardModule)
    }]
  },
  
  {
    path:'invoices',
    component: NavBarComponentComponent,
    canActivate: [AuthGuard],
    children: [{
      path:'',
      loadChildren: () => import('./pages/invoices/invoices.module').then(m => m.InvoicesModule)
    }]
  },

  {
    path: '*',
    redirectTo: 'dashboard/user',
    pathMatch: 'full'
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

