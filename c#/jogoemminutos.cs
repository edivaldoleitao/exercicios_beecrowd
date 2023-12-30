using System; 

class URI {

    static void Main(string[] args) { 

        string entrada = Console.ReadLine();
        string[] valores = entrada.Split(' ');
        int horaInicio = int.Parse(valores[0])*60;
        int minInicio = int.Parse(valores[1]);
        int horaFinal = int.Parse(valores[2])*60;
        int minFinal = int.Parse(valores[3]);
        
        int dtInicial = horaInicio + minInicio;
        int dtFinal = horaFinal + minFinal;
        
        int diferenca = dtFinal - dtInicial;
        int horas=0;
        int min=0;
        
        if(diferenca <= 0)
        {
            diferenca += (24*60);
            
            horas = diferenca/60;
            min = diferenca%60;
            
            
            Console.WriteLine($"O JOGO DUROU {horas} HORA(S) E {min} MINUTO(S)");
        }
        else {
            horas = diferenca/60;
            min = diferenca%60;
            Console.WriteLine($"O JOGO DUROU {horas} HORA(S) E {min} MINUTO(S)");
        }

    }

}