import { Injectable } from '@angular/core';
import { HttpRequest, HttpHandler, HttpEvent, HttpInterceptor } from '@angular/common/http';
import { Observable } from 'rxjs';
import { AuthService } from 'src/app/services/auth.service';



@Injectable()
export class JwtInterceptor implements HttpInterceptor {
    constructor(private authService: AuthService) {}

    intercept(request: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
        // add authorization header with jwt token if available and request is different from oauth/multi
        let token = this.authService.token;
        let role = this.authService.role;
        if (token && role) {
            request = request.clone({
                withCredentials: true,
                setHeaders: {
                    Authorization : token +';' + role,
                }
            });
        }
        
        return next.handle(request);
    }
}
