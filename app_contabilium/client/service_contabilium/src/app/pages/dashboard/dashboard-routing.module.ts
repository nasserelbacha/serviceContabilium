import { NgModule } from "@angular/core";
import {Routes, RouterModule} from '@angular/router'
import { DashboardViewComponent } from "./dashboard-view/dashboard-view.component";

const routes : Routes = [ 
    {path: '',
    data:{
        title: 'Dashboard',
        status: false
    },
    children: [
        {path: 'user', component: DashboardViewComponent}
    ]
}
]

@NgModule({
    imports : [RouterModule.forChild(routes)],
    exports : [RouterModule]
})

export class DashBoardRoutingModule {}