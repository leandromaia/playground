
Ext.define('App.exercices.Tocar',{

    tocar: function(){
        console.log('Tocando pela classe base ...');
    }
});

Ext.define('App.exercices.Afinar',{

    afinar: function(){
        console.log('Afinando pela classe base...');
    }
});

Ext.define('App.exercices.Eletrico',{

    obterEnergia: function(){
        console.log('Obtendo energia para funcionamento...');
    }
});


Ext.define('App.exercices.Violao',{
 
    constructor : function(options){
        console.log(options);

        this.obterEnergia(); 
    },

    extend : 'App.exercices.Eletrico',

    mixins :{
        first : 'App.exercices.Tocar',
        second : 'App.exercices.Afinar'
    }

});


Ext.onReady(function(){

    var violao = Ext.create('App.exercices.Violao','To constructor');
    violao.afinar();
    violao.tocar();
    
});