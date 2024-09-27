#include <iostream>
#include <cstring>
using namespace std;

struct Fantasma{ //Estructura base
    char tipo[20];
    int tiempoMuerto, altura;
    float temperatura;
    bool levitacion;
};

int main(){
    int numeroDeFantasmasAvistados = 2; //Variable estatica
    char* lugarDeAvistamiento = (char*)malloc(numeroDeFantasmasAvistados * sizeof(char));//Arreglo dinamico malloc
    for (int i=0;i<numeroDeFantasmasAvistados;i++){
        cout<<"Lugar donde fue visto: ";
        cin>>lugarDeAvistamiento[i];
    }

    Fantasma f1;//Estructura estatica
    strcpy(f1.tipo, "Oni");
    f1.tiempoMuerto = 3;
    f1.altura = 178;
    f1.temperatura = -1.5;
    f1.levitacion = false;

    class f2{//Clase dinamica new
    public:
        char* tipo;
        int tiempoMuerto, altura;
        float temperatura;
        bool levitacion;

        f2(const char* tip, int tm, int al, float temp, bool lev){
            tipo = new char(strlen(tip)+1);
            strcpy(tipo, tip);
            tiempoMuerto = tm;
            altura = al;
            temperatura = temp;
            levitacion = lev;
        }

        ~f2(){
            delete[] tipo;
        }
    };

    f2* f2admin = new f2("Demonio", 6, 215, 4.2, false);




    cout<<"Fantasmas avistados: "<<numeroDeFantasmasAvistados<<endl;
    cout<<"Lugares de los avistamientos: ";
    for (int i=0; i<numeroDeFantasmasAvistados;i++){
        cout<<lugarDeAvistamiento[i]<<" ";
    }
    cout<<endl;
    cout<<"\nFantasma 1: \nTipo: "<<f1.tipo<<"\nAnos muerto: "<<f1.tiempoMuerto<<"\nAltura: "<<f1.altura<<"\nTemperatura: "<<f1.temperatura<<"\nLevitacion: "<<f1.levitacion<<endl;
    cout<<"\nFantasma 2: \nTipo: "<<f2admin->tipo<<"\nAnos muerto: "<<f2admin->tiempoMuerto<<"\nAltura: "<<f2admin->altura<<"\nTemperatura: "<<f2admin->temperatura<<"\nLevitacion: "<<f2admin->levitacion<<endl;

    delete[] lugarDeAvistamiento;
    delete f2admin;

return 0;
};
