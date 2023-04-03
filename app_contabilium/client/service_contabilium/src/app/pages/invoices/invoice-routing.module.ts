import { NgModule } from "@angular/core";
import {Routes, RouterModule} from '@angular/router'
import { LoadInvoiceComponent } from "./load-invoice/load-invoice.component";


const routes : Routes = [ 
    {path: '',
    data:{
        title: 'Invoices',
        status: true
    },
    children : [
        {path: 'load-invoice', component: LoadInvoiceComponent}
    ]
}
]

@NgModule({
    imports : [RouterModule.forChild(routes)],
    exports : [RouterModule]
})

export class InvoiceRoutingModule {}