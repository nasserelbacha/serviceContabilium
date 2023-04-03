import { Component, OnInit } from '@angular/core';
import { ProviderService } from '../../services/providers.service';
import { AuthService } from '../../services/auth.service';
import { MatDialog, MatDialogConfig } from '@angular/material/dialog';
import { LogInDialogComponent } from './log-in-dialog/log-in-dialog.component';
import { NavItems, Nav_Items } from '../nav-items/nav-items';
import { NavigationEnd, Router } from '@angular/router';

@Component({
  selector: 'app-nav-bar-component',
  templateUrl: './nav-bar-component.component.html',
  styleUrls: ['./nav-bar-component.component.css']
})
export class NavBarComponentComponent implements OnInit {

  constructor(
   private authService: AuthService,
   private dialog : MatDialog,
   private navItems : NavItems,
   private router: Router
  ) { }

  userIsLog : boolean = false;
  items : Array<any>
  sectionScroll : string | null | undefined;

  ngOnInit(): void {
    if(localStorage.getItem('token')){
      this.userIsLog = true
    }
    this.getItems()
    this.router.events.subscribe((evt) => {
      if (!(evt instanceof NavigationEnd)) {
        return;
      }
      this.doScroll();
      this.sectionScroll= null;
    });

  }

  getItems(){
    this.items = this.navItems.getAll()
  }

  async log(){
    const dialogConfig = new MatDialogConfig()
    dialogConfig.width = '30vw'
    const dialogRef = this.dialog.open(LogInDialogComponent, dialogConfig).afterClosed().subscribe((res) => {
      
    })
  }

  async logOut(){
    this.userIsLog = false
    await this.authService.logOut()
    await this.authService.redirectLogin()
  }

  navigateNav(item: Nav_Items){
    this.sectionScroll = item.params;
    this.router.navigate([item.route], {
      fragment: item.params
    })
  }

  doScroll(){
    if (!this.sectionScroll) {
      return;
    }
    try {
      const  elements = document.getElementById(this.sectionScroll);
      if(elements){
        elements.scrollIntoView();
      }
    }
    finally{
      this.sectionScroll = null;
    }
  }

}
