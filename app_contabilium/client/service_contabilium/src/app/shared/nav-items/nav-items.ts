import { Injectable } from "@angular/core"

export interface Nav_Items{
    name: string,
    route: string,
    manager: boolean,
    userAuth: boolean,
    params? : string
}

const NAV_ITEMS = [
    {
        name: "Contacto",
        route: "/dashboard/user",
        manager: false,
        params: "contact",
        userAuth: false
    }, {
        name: "Precios",
        route: "/dashboard/user",
        params: "prices",
        manager: false,
        userAuth: false
    },  
    {
        name: "¿Quienes Somos?",
        route: "/dashboard/user",
        params: "us",
        manager: false,
        userAuth: false
    },
    {
        name: "Facturas",
        route: "/invoices/load-invoice",
        manager: false,
        userAuth: true
    },
    
]

@Injectable()
export class NavItems{
    getAll() : Nav_Items[] {
        return NAV_ITEMS;
    }
}