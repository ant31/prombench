local kpm = import "kpm.libjsonnet";

function(
  params={}
)

kpm.package({
   package: {
      name: "ant31/prombench",
      expander: "jinja2",
      author: "Antoine Legrand",
      version: "0.0.1-1",
      description: "prombench",
      license: "Apache 2.0",
    },

    variables: {
      appname: "prombench",
      namespace: 'default',
      image: "quay.io/ant31/prombench:v0.0.1",
      svc_type: "LoadBalancer",
    },

    resources: [
      {
        file: "prombench-dp.yaml",
        template: (importstr "templates/prombench-dp.yaml"),
        name: "prombench",
        type: "deployment",
      },

      {
        file: "prombench-svc.yaml",
        template: (importstr "templates/prombench-svc.yaml"),
        name: "prombench",
        type: "service",
      }
      ],


    deploy: [
      {
        name: "$self",
      },
    ],


  }, params)
