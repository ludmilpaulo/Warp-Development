import React, { useState } from "react";
import { View, Text, TouchableOpacity, ActivityIndicator } from "react-native";
import { useLazyExecuteSubmissionQuery } from "../redux/apiSlice";
import tw from "../tw"; 

export default function HomeScreen() {
  const [trigger] = useLazyExecuteSubmissionQuery();
  const [loading, setLoading] = useState(false);
  const [status, setStatus] = useState("");

  const handleSubmission = async () => {
    setLoading(true);
    setStatus("");
    try {
      const res = await trigger().unwrap();
      setStatus(res.status);
    } catch {
      setStatus("Submission Failed");
    } finally {
      setLoading(false);
    }
  };

  return (
    <View style={tw`flex-1 bg-gray-100 justify-center items-center px-6`}>
      <View style={tw`bg-white p-8 rounded-3xl shadow-lg w-full`}>
        <Text style={tw`text-3xl font-bold text-gray-800 text-center mb-4`}>
          Submit Your CV
        </Text>
        <Text style={tw`text-center text-gray-600 mb-6`}>
          Press the button below to securely submit your CV.
        </Text>

        <TouchableOpacity
          disabled={loading}
          onPress={handleSubmission}
          style={tw`py-3 rounded-xl ${
            loading ? "bg-gray-400" : "bg-indigo-600"
          }`}
        >
          <Text style={tw`text-white font-semibold text-center text-lg`}>
            {loading ? "Submitting..." : "Submit CV"}
          </Text>
        </TouchableOpacity>

        {status ? (
          <View style={tw`mt-5 py-3 px-4 bg-green-100 rounded-lg`}>
            <Text style={tw`text-green-700 font-semibold text-center`}>
              {status === "Success"
                ? "🎉 CV submitted successfully!"
                : "⚠️ " + status}
            </Text>
          </View>
        ) : null}
      </View>

      {/* Loading overlay */}
      {loading && (
        <View style={tw`absolute inset-0 bg-black bg-opacity-50 justify-center items-center`}>
          <ActivityIndicator size="large" color="#ffffff" />
        </View>
      )}
    </View>
  );
}
