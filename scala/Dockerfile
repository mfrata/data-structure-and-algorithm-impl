 FROM openjdk:8 as sbt

 WORKDIR /dsalgo

 RUN \
   echo "deb https://repo.scala-sbt.org/scalasbt/debian all main" \
   | tee /etc/apt/sources.list.d/sbt.list \
   echo "deb https://repo.scala-sbt.org/scalasbt/debian /" \
   | tee /etc/apt/sources.list.d/sbt_old.list \
   && curl -sL "https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x2EE0EA64E40A89B84B2DF73499E82A75642AC823" \
   | apt-key add \
   && apt update && apt install sbt -y \
   && apt-get autoremove -y \
   && apt-get -y clean \
   && rm -rf "/tmp/"* \
   "/var/cache/apt" \
   "/usr/share/man" \
   "/usr/share/doc" \
   "/usr/share/doc-base" \
   "/usr/share/info/*"


FROM sbt as project

COPY project project
COPY build.sbt build.sbt

RUN mkdir -p src/main/scala && \
    echo 'object Main {def main(a: Array[String]) {}}' > src/main/scala/Main.scala

RUN sbt update && sbt test && sbt compile
