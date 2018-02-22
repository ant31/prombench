local utils = (import "jpy-utils.libsonnet");
{
  images: {
    release: {
      promsnaps: {
        creds: {
          host: "quay.io",
          password: "$QUAY_TOKEN",
          username: "promsnaps+gitlabci",
        },
        repo: "quay.io/ant31/promsnaps",
        tag: "${CI_COMMIT_REF_SLUG}-${SHA8}",
        name: utils.docker.containerName(self.repo, self.tag),
        get_name(tag):: utils.docker.containerName(self.repo, tag),
      },
    },
    ci: {
      promsnaps: {
        creds: {
          host: "quay.io",
          password: "$QUAY_TOKEN",
          username: "promsnaps+gitlabci",
        },
        repo: "quay.io/ant31/promsnaps",
        tag: "ci-${CI_COMMIT_REF_SLUG}-${SHA8}",
        name: utils.docker.containerName(self.repo, self.tag),
        get_name(tag):: utils.docker.containerName(self.repo, tag),
      },
    },
  },
}
