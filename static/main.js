const { createApp } = Vue;

const Taskapp = {
  data() {
    return {
      task: {
        name: "",
      },
      tasks: [],
    };
  },
  async created() {
    await this.getTasks();
  },
  methods: {
    async sendRequest(url, method, data) {
      const myHeaders = new Headers({
        "Content-Type": "application/json",
        "X-Requsted-With": "XMLHttpRequest",
      });

      const response = await fetch(url, {
        method: method,
        headers: myHeaders,
        body: data,
      });

      return response;
    },
    async getTasks() {
      const response = await this.sendRequest(window.location,'get')
      this.tasks = await response.json();
    },
    async createTask() {
      await this.getTasks();
      await this.sendRequest(window.location + 'create','post',
      JSON.stringify(this.task))
      await this.getTasks();

      this.task.name = "";
    },
  },
  delimiters: ["{", "}"],
};

createApp(Taskapp).mount("#app");
