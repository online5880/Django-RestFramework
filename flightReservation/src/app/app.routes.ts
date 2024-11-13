import { Routes } from '@angular/router';
import { FindFlightComponent } from './components/find-flight/find-flight.component';
import { DisplayFlightsComponent } from './components/display-flights/display-flights.component';
import { PassengerDetailsComponent } from './components/passenger-details/passenger-details.component';
import { ConfirmComponent } from './components/confirm/confirm.component';

export const routes: Routes = [
    {path:'',redirectTo:'',pathMatch:'full'},
    {
        path : 'findFlights',
        component: FindFlightComponent
    },
    {
        path : 'displayFlights',
        component: DisplayFlightsComponent
    },
    {
        path : 'passengerDetails/:id',
        component: PassengerDetailsComponent
    },
    {
        path : 'confirm/:id',
        component: ConfirmComponent
    },
];
