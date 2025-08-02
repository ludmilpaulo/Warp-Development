'use client';

import { useLazyExecuteSubmissionQuery } from '@/redux/apiSlice';
import { useState } from 'react';
import { Transition } from '@headlessui/react';

export default function Home() {
  const [trigger] = useLazyExecuteSubmissionQuery();
  const [loading, setLoading] = useState(false);
  const [status, setStatus] = useState('');

  const handleSubmission = async () => {
    setLoading(true);
    setStatus('');
    console.log("🚀 Submission initiated");
    try {
      const res = await trigger().unwrap();
      console.log("✅ API response:", res);
      setStatus(res.status);
    } catch (error) {
      console.error("❌ API error:", error);
      setStatus('Failed to submit CV.');
    } finally {
      setLoading(false);
      console.log("🔄 Loading state ended");
    }
  };

  return (
    <main className="flex items-center justify-center min-h-screen bg-gray-50">
      <div className="bg-white shadow-xl rounded-2xl p-8 max-w-lg w-full text-center">
        <h1 className="text-3xl font-bold mb-4 text-gray-800">CV Submission</h1>
        <p className="mb-6 text-gray-600">
          Click below to securely submit your CV and application details.
        </p>
        <button
          onClick={handleSubmission}
          disabled={loading}
          className="bg-indigo-600 hover:bg-indigo-700 text-white font-semibold py-3 px-8 rounded-lg transition duration-300 disabled:bg-gray-400 disabled:cursor-not-allowed"
        >
          Submit CV
        </button>

        {status && (
          <div className="mt-5 py-3 px-4 bg-green-100 text-green-700 rounded-lg font-semibold shadow animate-pulse">
            {status === 'Success'
              ? '🎉 Your CV was submitted successfully!'
              : `⚠️ ${status}`}
          </div>
        )}
      </div>

      {/* Loading Overlay */}
      <Transition
        show={loading}
        enter="transition-opacity duration-300"
        enterFrom="opacity-0"
        enterTo="opacity-100"
        leave="transition-opacity duration-300"
        leaveFrom="opacity-100"
        leaveTo="opacity-0"
      >
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-50">
          <div className="w-16 h-16 border-t-4 border-b-4 border-white rounded-full animate-spin"></div>
        </div>
      </Transition>
    </main>
  );
}
