from client import StudioGradeAcousticVoiceIsolationDenoiserClient

def main():
    client = StudioGradeAcousticVoiceIsolationDenoiserClient()
    res = client.isolate_and_denoise_audio_track('https://assets.genpark.ai/audio/cafe_podcast_background_chatter.wav', 0.98)
    print('Isolation Job: ' + res['isolation_job_id'] + ' (Latency: ' + str(res['realtime_processing_latency_ms']) + 'ms)')
    print('SNR Improvement: +' + str(res['snr_signal_to_noise_improvement_db']) + ' dB | Reverb Elimination: ' + str(res['room_reverberation_elimination_pct']) + '%')
    print('Harmonic Preservation: ' + str(res['speech_harmonic_preservation_score']) + '%')
    print('Isolated Audio URL: ' + res['studio_flac_audio_output_url'])

if __name__ == '__main__':
    main()
