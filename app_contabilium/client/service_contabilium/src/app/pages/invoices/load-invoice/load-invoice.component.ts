import { Component, OnInit, ViewChild } from '@angular/core';
import { ImageCroppedEvent } from '../image-cropper/image-cropper/interfaces';
import { ImageCropperComponent } from '../image-cropper/image-cropper/image-cropper.component';
import { TestService } from 'src/app/services/test.service';
@Component({
  selector: 'app-load-invoice',
  templateUrl: './load-invoice.component.html',
  styleUrls: ['./load-invoice.component.css']
})
export class LoadInvoiceComponent implements OnInit {

  constructor(private testService : TestService){}

  ngOnInit(): void {
  }

  imageChangedEvent: any = '';
  croppedImage: any = '';
  showCropper = false;

  @ViewChild(ImageCropperComponent) imageCropper: ImageCropperComponent;

  fileChangeEvent(event: any): void {
      this.imageChangedEvent = event;
  }
  imageCropped(event: ImageCroppedEvent) {
    this.croppedImage = event.base64;
    console.log(event);
  }
  imageLoaded() {
    this.showCropper = true;
     console.log('Image loaded')
  }
  cropperReady() {
    console.log('Cropper ready')
  }
  loadImageFailed () {
    console.log('Load failed');
  }

  async test(){
    await this.testService.test().subscribe((res) => {
      console.log(res)
    })
  }

}
