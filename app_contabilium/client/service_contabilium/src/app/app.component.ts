import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'service_contabilium';

  file : any
  cardImageBase64 : any


async onFileChanged(event : any) {
  // verificar que tipo de archivo es
  // si es pdf hacer el cambio a .png, una vez que ya esta seguimos
  // sino seguir con la funcion
    this.file = event.target.files[0]
    if (event.target.files && this.file){
      const reader = new FileReader();
      reader.onload = (e: any) => {
        const image = new Image();
        image.src = e.target.result;
        image.onload = rs => {
          const imgBase64Path = e.target.result;
          this.cardImageBase64 = imgBase64Path;         
          // this.imageChange = true;
        };
      };
      reader.readAsDataURL(this.file);
    }
  }
}

