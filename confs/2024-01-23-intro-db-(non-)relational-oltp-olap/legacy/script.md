# Introducción a las Bases de Datos

## Sistemas de Información



¿Qué tan grande es YouTube?

No lo sabemos, en la actualidad no se conoce la cifra exacta de horas de video o cantidad de videos que contiene YouTube. Sin embargo, sí existen datos que nos permiten imaginar la inmensidad de la plataforma. Cada minuto más de 500 horas de video son subidas a YouTube, haciendo unos cálculos obtenemos que un total de 720000 horas son subidas cada día. Por lo que nos tomaría unos 82 años, casi una vida entera, para ver todo el contenido subido a la plataforma en un solo día :open_mouth:.​ 

Hoy en día es común estar en contacto con plataformas que almacenan y utilizan cantidades masivas de datos. Muchas personas utilizan redes sociales como Facebook e Instagram para compartir sus recuerdos y experiencias con las demás personas, otras utilizan YouTube para buscar vídeos con los que aprender y divertirse e, incluso, para algunas personas plataformas como Amazon desempeñan un papel fundamental en su forma de ganarse la vida.

La disciplina de sistemas de información, en la cual se enmarca esta asignatura, tiene como objetivo permitirles entender cuáles son las bases del funcionamiento de los sistemas utilizados por estas plataform as en particular y por cualquier organización que almacene y utilice datos en general.

## Motivación de la asignatura

Hasta ahora puede parecer que el propósito de esta asignatura es muy distinto al de otras que han visto previamente en la carrera, pero en realidad, también estamos aquí para resolver problemas, en particular dos problemas que los limitan mucho como programadores y científicos de la computación.

- **Asegurar la persitencia de los datos generados por aplicaciones y dispositivos**: osea que los datos se mantengan en memoria externa incluso luego de terminada la ejecución del programa.

- **Utilizar grandes cantidades de datos de forma eficiente**: sin poder contar con almacenamiento externo los programas están limitados por la capacidad de la memoria RAM de la computadora.

## ¿Cómo?

Mmmmm esta asignatura se llama **Bases de Datos** así que obviamente la respuesta es bases de datos:thinking:, probablemente estarán pensando. Sin embargo, todos almacenamos datos en nuestra computadora y no utilizamos una base de datos para ello. Guardamos los documentos de la universidad, nuestras fotos personales, la música que nos gusta y las series que vemos. La realidad es que el simple hecho de tener datos no es una razón los suficientemente buena para utilizar una base de datos. Por ejemplo, si quiero guardar los datos de los estudiantes de este curso no voy a utilizar una base de datos sino un fichero (un excel) y los voy a escribir ahí. De hecho muchas empresas hacen (o han hecho) esto, pero, a medida que las empresas crecen también suelen crecer las cantidades de datos que estas manejan, y lo que antes era un fichero con unos pocos cientos de líneas se puede convertir en miles de ficheros con millones de líneas.

## Sistemas orientados a ficheros

Este tipo de sistemas para el almacenamiento de datos se les llama sistemas orientados a ficheros. Y si bien técnicamente funcionan tienen muchas carencias. Se imaginan estar en un aeropuerto apurados por coger un vuelo y la persona que debe buscar por donde sale nuestro vuelo debe de buscar esa información dentro de miles de ficheros.  

## Base de Datos

Entonces ya que sabemos por qué queremos una base de datos es hora de saber qué son. 

Formalmente "... *una base de datos es una colección autodescriptiva de registros integrados*" -- C. J. Date

Analicemos cada uno de los elementos de esta definición:

- Un registro contiene datos específicos, por ejemplo los datos de una persona en particular. 

- Esta colección es **autodescriptiva** porque dentro de la propia base de datos se almacenan metadatos sobre la estructura de los registros almacenados. Por ejemplo, los datos de una persona podrían ser su nombre (`string`), apellido (`string`), correo (`string`), edad(`int`), peso(`float`) y altura(`float`). 
- Estos registros se **integran** a través de las relaciones entre los datos, por ejemplo, en redes sociales una persona puede ser amigo de otras   personas, en un banco una persona puede ser dueño de varias cuentas bancarias, etc.

Informalmente las bases de datos son... ficheros, entonces ¿Cómo pueden solucionar las limitaciones de los sistemas orientados a ficheros?

## Un cambio de enfoque

La principal causa de las limitaciones de los sistemas orientados a ficheros es que son los seres humanos quienes se encargan de cómo almacenar y manipular los datos (ya sea utilizando *software* que les permita modificar los archivos manualmente o mediante código). Es el usuario quien decide en cuál fichero escribir cada registro, cómo deben estar ordenados los ficheros, cómo obtener la información buscada, etc. Este enfoque es el mismo que se utilizaba años atrás cuando los datos se almacenaban en papel y este era el problema: la tecnología para el almacenamiento de datos había evolucionado, ahora almacenábamos los datos de forma digital, sin embargo, el enfoque sobre cómo almacenar y manipular los datos no había evolucionado. Los humanos seguíamos teniendo el control sobre los datos y simplemente nuestro cerebro no tiene la capacidad para manejar cantidades masivas de datos. Las bases de datos resuelven las limitaciones de los sistemas orientados a ficheros cediendo el control sobre los datos a un *software* que se encarga de cómo almacenar y manipular dichos datos.

## Sistema Gestor de Bases de Datos

Este *software* es llamado Sistema Gestor de Bases de Datos y son definidos como 

"... *un sistema computacional que proporciona funcionalidades, medios o servicios para manipular y, en particular, manejar todos los accesos a una base de datos o una colección de bases de datos* 

Estos sistemas cumplen una serie de propiedades que los vuelven

- Persistencia: Los datos permanecen en almacenamiento externo incluso luego de terminada la ejecución del programa.
- Masivos: Manejan terabytes/petabytes de datos en memoria externa.
- Eficientes: Implementan de forma eficiente las operaciones sobre los datos gracias a la utilización de estructuras de datos y algoritmos eficientes.
- Multi-Usuarios: Múltiples usuarios (aplicaciones o personas) pueden operar simultáneamente sobre los mismos datos gracias a la implementación de protocolos para manejar la concurrencia.
- Seguros: Mantienen un estado consistente de la base de datos ante fallos de hardware, software, electricidad o intentos de acceso por usuarios no autorizados.
- Confiables: Garantía de disponibilidad al 99.99999%
- Convenientes: