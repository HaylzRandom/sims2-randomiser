import { useEffect, useState } from 'react';

const hairColours = ['blonde', 'black', 'brown', 'red'];
const eyeColoursMin = 1;
const eyeColoursMax = 5;
const skinTonesMin = 1;
const skinTonesMax = 24;
const eyebrowsMin = 1;
const eyebrowsMax = 4;

const SimInfo = ({ gender, generateSim }) => {
	const [hairColour, setHairColour] = useState('blonde');
	const [name, setName] = useState('John Smith');
	const [glasses, setGlasses] = useState(false);
	const [beard, setBeard] = useState(false);
	const [eyeColour, setEyeColour] = useState(1);
	const [skinTone, setSkinTone] = useState(1);
	const [eyebrows, setEyebrows] = useState(1);

	useEffect(() => {
		wearGlasses();
		hasBeard();
		generateEyeColour();
		generateSkinTone();
		generateEyebrows();
		generateHairColour();
	}, [generateSim]);

	const wearGlasses = () => {
		setGlasses(Math.random() > 0.5 ? true : false);
	};

	const hasBeard = () => {
		if (gender === 'male') {
			setBeard(Math.random() > 0.5 ? true : false);
		} else {
			setBeard(false);
		}
	};

	const generateEyeColour = () => {
		setEyeColour(
			Math.floor(Math.random() * (eyeColoursMax - eyeColoursMin + 1)) +
				eyeColoursMin
		);
	};

	const generateSkinTone = () => {
		setSkinTone(
			Math.floor(Math.random() * (skinTonesMax - skinTonesMin + 1)) +
				skinTonesMin
		);
	};

	const generateEyebrows = () => {
		setEyebrows(
			Math.floor(Math.random() * (eyebrowsMax - eyebrowsMin + 1)) + eyebrowsMin
		);
	};

	const generateHairColour = () => {
		setHairColour(hairColours[Math.floor(Math.random() * hairColours.length)]);
	};

	return (
		<section id='sim__info'>
			<header>
				<h2>Sim Info</h2>
			</header>
			<div className='sim-info'>
				<ul className='sim-info__info'>
					<li>
						<p>
							<span className='title'>Name: </span>
							{name}
						</p>
					</li>
					<li>
						<p>
							<span className='title'>Skin: </span>
							{skinTone}
						</p>
					</li>
					<li>
						<p>
							<span className='title'>Eyes: </span>
							{eyeColour}
						</p>
					</li>
					<li>
						<p>
							<span className='title'>Hair Colour: </span>
							{hairColour}
						</p>
					</li>
					<li>
						<p>
							<span className='title'>Eyebrows: </span>
							{eyebrows}
						</p>
					</li>
					<li>
						<p>
							<span className='title'>Glasses: </span>
							{glasses.toString()}
						</p>
					</li>
					{gender === 'male' && (
						<li className='info__beard'>
							<p>
								<span className='title'>Beard: </span>
								{beard.toString()}
							</p>
						</li>
					)}
				</ul>
			</div>
		</section>
	);
};
export default SimInfo;
