import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { LoadInvoiceComponent } from './load-invoice/load-invoice.component';
import { ImageCropperModule } from './image-cropper/image-cropper/image-cropper.module';
import { InvoiceRoutingModule } from './invoice-routing.module';

@NgModule({
  imports: [
    CommonModule,
    ImageCropperModule,
    InvoiceRoutingModule
  ],
  declarations: [LoadInvoiceComponent],
})
export class InvoicesModule { }
