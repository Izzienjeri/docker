const id = 123; // Mocked ID
const headers = { Authorization: "Bearer token" }; // Mocked headers
import { toast } from "react-toastify";
import axios from "axios";
export const f = (values, { resetForm }) => {
  console.log(values);
  values.ipd_enrollment_id = id; // Assume id is defined
  axios
    .post("/api/doctor/ipd_enrollement_bill_items/create", values, headers) // Assume headers is defined
    .then((response) => {
      console.log(response.data);
      const message = response.data.message;
      if (response.data.status) {
        resetForm(); // Reset the form immediately
        toast.success(message, {
          autoClose: 1000,
        });
      } else {
        toast.error(message, {
          autoClose: 2000,
        });
      }
    })
    .catch((error) => {
      console.log(error);
    });
};