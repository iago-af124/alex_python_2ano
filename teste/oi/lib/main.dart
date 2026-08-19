import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      home: const MyHomePage(),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key});

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {


  void alerta(String msg){
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        content: Text(msg),
        duration: Duration(seconds: 5),
      ),
    );
  }
  
  bool tf = false;
  void Switchvoid(bool valor){
    setState(() {
      tf = valor;
      print(tf);
    });
  }

  bool tf2 = false;
  void CheckBoxvoid(bool? valor2){
    setState(() {
      tf2 = valor2 ?? false;
      print(tf2);
    });
  }

  double valor = 0;
  void valorslide(double v){
    setState(() {
      valor = v;
      alerta(v.toString());
    });
  }


  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: Column(
          children: [
            Text('Teste'),
            Text('Switch'),
            Switch(value: tf, onChanged: Switchvoid),
            Text('Checkbox'),
            Checkbox(value: tf2, onChanged: CheckBoxvoid),
            Text('Slider'),
            Slider(value: valor, min:0, max:100 , onChanged: valorslide)
          ],
        ),
      )
    );
  }
}
