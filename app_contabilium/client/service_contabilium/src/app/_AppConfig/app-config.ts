import { HttpHeaders } from '@angular/common/http';
import { environment } from '../../environments/environment';

export class AppConfig{
    public static API_ENDPOINT = environment.SERVER_URL + "/core"
    public static COMPANIES = this.API_ENDPOINT + "/companies"

}