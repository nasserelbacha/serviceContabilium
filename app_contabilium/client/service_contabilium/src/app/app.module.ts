import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { ImageCropperModule } from './pages/image-cropper/image-cropper/image-cropper.module';
import { AppComponent } from './app.component';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { LoadInvoiceComponent } from './pages/load-invoice/load-invoice.component';
import { RouterModule } from '@angular/router';
import { MaterialModule } from './material/material.module';
import { SharedModule } from './shared/shared.module';
import { AppRoutingModule } from './app-routing.module';


@NgModule({
  declarations: [
    AppComponent,
    LoadInvoiceComponent,
  ],
  imports: [
    BrowserModule,
    ImageCropperModule,
    HttpClientModule,
    RouterModule.forRoot([]),
    MaterialModule,
    SharedModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
